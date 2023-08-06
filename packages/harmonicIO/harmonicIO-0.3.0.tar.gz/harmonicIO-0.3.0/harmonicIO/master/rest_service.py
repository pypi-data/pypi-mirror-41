import falcon
from .configuration import Setting
from harmonicIO.general.definition import Definition, CStatus, CRole
from .messaging_system import MessagesQueue
from harmonicIO.general.services import SysOut, Services as LService
from .meta_table import LookUpTable


class RequestStatus(object):

    def __init__(self):
        pass

    def on_get(self, req, res):
        """
        GET: /status?token={None}
        """
        if not Definition.get_str_token() in req.params:
            res.body = "Token is required."
            res.content_type = "String"
            res.status = falcon.HTTP_401
            return

        if req.params[Definition.get_str_token()] == Setting.get_token():

            result = LService.get_machine_status(Setting, CRole.MASTER)

            res.body = str(result)
            res.content_type = "String"
            res.status = falcon.HTTP_200
        else:
            res.body = "Invalid token ID."
            res.content_type = "String"
            res.status = falcon.HTTP_401

    def on_put(self, req, res):
        """
        PUT: /status?token={None}
        """
        if not Definition.get_str_token() in req.params:
            res.body = "Token is required."
            res.content_type = "String"
            res.status = falcon.HTTP_401
            return

        if req.params[Definition.get_str_token()] == Setting.get_token():
            raw = str(req.stream.read(), 'UTF-8')
            data = eval(raw)

            LookUpTable.update_worker(data)
            SysOut.debug_string("Update worker status ({0})".format(data[Definition.get_str_node_name()]))

            res.body = "Okay"
            res.content_type = "String"
            res.status = falcon.HTTP_200
        else:
            res.body = "Invalid token ID."
            res.content_type = "String"
            res.status = falcon.HTTP_401


class MessageStreaming(object):
    def __init__(self):
        pass

    def on_get(self, req, res):
        """
        return "&c_name=" + container_name + "&c_os=" + container_os + "&priority=" + str(priority)
        GET: /streamRequest?token=None
        This function is mainly respond with the available channel for streaming from data source.
        """

        if not Definition.get_str_token() in req.params:
            res.body = "Token is required."
            res.content_type = "String"
            res.status = falcon.HTTP_401
            return

        # Check for required parameter.
        if not Definition.Container.get_str_con_image_name() in req.params:
            res.body = "Container name is required."
            res.content_type = "String"
            res.status = falcon.HTTP_401
            return

        if not Definition.Container.get_str_container_os() in req.params:
            res.body = "Container os is required."
            res.content_type = "String"
            res.status = falcon.HTTP_401
            return

        if not Definition.Container.get_str_data_source() in req.params:
            res.body = "Data digest is required."
            res.content_type = "String"
            res.status = falcon.HTTP_401
            return

        # Parse to dict object
        ret = LookUpTable.Tuples.get_tuple_object(req)

        if Definition.Container.get_str_container_priority() in req.params:
            if LService.is_str_is_digit(req.params[Definition.Container.get_str_container_priority()]):
                ret[Definition.Container.get_str_container_priority()] = int(req.params[Definition.Container.get_str_container_priority()])

            else:
                res.body = "Container priority is not digit."
                res.content_type = "String"
                res.status = falcon.HTTP_401
                return

        # Register item into tuples
        LookUpTable.Tuples.add_tuple_info(ret)

        # Check for the availability of the container
        ret = LookUpTable.get_candidate_container(ret[Definition.Container.get_str_con_image_name()])

        if ret:
            res.body = Definition.Master.get_str_end_point(ret)
            res.content_type = "String"
            res.status = falcon.HTTP_200
            return
        else:
            # No streaming end-point available
            res.body = Definition.Master.get_str_end_point_MS(Setting)
            res.content_type = "String"
            res.status = falcon.HTTP_200
            return

    def on_post(self, req, res):
        """
        POST: /streamRequest?token=None
        This function invoked by the driver in micro-batch in the container.
        It responds with getting a stream from data source or from messaging system.
        """
        if not Definition.get_str_token() in req.params:
            res.body = "Token is required."
            res.content_type = "String"
            res.status = falcon.HTTP_401
            return

        # Check that the PE is existing or not, if not insert and respond
        if Definition.REST.Batch.get_str_batch_addr() in req.params and \
           Definition.REST.Batch.get_str_batch_port() in req.params and \
           Definition.REST.Batch.get_str_batch_status() in req.params and \
           Definition.Container.get_str_con_image_name() in req.params:

            # Check for data type
            if req.params[Definition.REST.Batch.get_str_batch_port()].isdigit() and \
               req.params[Definition.REST.Batch.get_str_batch_status()].isdigit():

                ret = LookUpTable.Containers.get_container_object(req)

                # If queue contain data, ignore update and stream from queue
                length = MessagesQueue.get_queues_length(ret[Definition.Container.get_str_con_image_name()])

                if not length:
                    LookUpTable.Containers.update_container(ret)
                    SysOut.debug_string("No item in queue!")
                    res.body = "No item in queue"
                    res.content_type = "String"
                    res.status = falcon.HTTP_200
                    return

                if length > 0 and ret[Definition.REST.Batch.get_str_batch_status()] == CStatus.AVAILABLE:
                    # ret[Definition.REST.Batch.get_str_batch_status()] = CStatus.BUSY
                    # LookUpTable.Containers.update_container(ret)

                    res.data = bytes(MessagesQueue.pop_queue(ret[Definition.Container.get_str_con_image_name()]))
                    res.content_type = "Bytes"
                    res.status = falcon.HTTP_203
                    return
                else:
                    # Register a new channel
                    LookUpTable.Containers.update_container(ret)
                    res.body = "OK"
                    res.content_type = "String"
                    res.status = falcon.HTTP_200
                    return
            else:
                res.body = "Invalid data type!"
                res.content_type = "String"
                res.status = falcon.HTTP_406
                return
        else:
            res.body = "Invalid parameters!"
            res.content_type = "String"
            res.status = falcon.HTTP_406
            return


class MessagesQuery(object):
    def __init__(self):
        pass

    def on_get(self, req, res):
        """
        GET: /messagesQuery?token=None&command=queueLength
         This function inquiry about the number of messages in queue. For dealing with create a new instance.
        """
        if not Definition.get_str_token() in req.params:
            res.body = "Token is required."
            res.content_type = "String"
            res.status = falcon.HTTP_401
            return

        if not Definition.MessagesQueue.get_str_command() in req.params:
            res.body = "No command specified."
            res.content_type = "String"
            res.status = falcon.HTTP_406
            return

        if req.params[Definition.MessagesQueue.get_str_command()] == Definition.MessagesQueue.get_str_queue_length():
            res.body = str(MessagesQueue.get_queues_all())
            res.content_type = "String"
            res.status = falcon.HTTP_200
            return

        if req.params[Definition.MessagesQueue.get_str_command()] == Definition.MessagesQueue.get_str_current_id():
            res.body = "None"
            res.content_type = "String"
            res.status = falcon.HTTP_200
            return

        if req.params[Definition.MessagesQueue.get_str_command()] == "verbose":
            data = LookUpTable.verbose()
            data['MSG'] = MessagesQueue.verbose()

            res.body = str(data)
            res.content_type = "String"
            res.status = falcon.HTTP_200

        if req.params[Definition.MessagesQueue.get_str_command()] == "verbose_html":
            data = LookUpTable.verbose()
            data['MSG'] = MessagesQueue.verbose()

            res.body = get_html_form(data['WORKERS'], data['MSG'], data['CONTAINERS'], data['TUPLES'])
            res.content_type = "String"
            res.status = falcon.HTTP_200

class RESTService(object):
    def __init__(self):
        # Initialize REST Services
        from wsgiref.simple_server import make_server
        api = falcon.API()

        # Add route for getting status update
        api.add_route('/' + Definition.REST.get_str_status(), RequestStatus())

        # Add route for stream request
        api.add_route('/' + Definition.REST.get_str_stream_req(), MessageStreaming())

        # Add route for msg query
        api.add_route('/' + Definition.REST.get_str_msg_query(), MessagesQuery())

        # Establishing a REST server
        self.__server = make_server(Setting.get_node_addr(), Setting.get_node_port(), api)

    def run(self):
        SysOut.out_string("REST Ready.....")

        self.__server.serve_forever()


def get_html_form(worker, msg, containers, tuples):
    html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>HarmonicIO: Dashboard (Debug)</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
    <!-- Custom styles for this template -->
    <link href="sticky-footer-navbar.css" rel="stylesheet">
  </head>

  <body>

    <!-- Fixed navbar -->

    <!-- Begin page content -->
    <div class="container">
      <div class="mt-3">
        <h1>Harmonic IO: Dashboard (Debug)</h1>
      </div>
      <p class="lead">System probe and status checking. (Not Auto Refresh!)</p>
    <section>
      <br>
      <h3>Worker Status</h3>
      <table class="table table-striped">
        <thead>
          <tr><th>Name</th><th>Address</th><th>Dockers</th><th>Loads</th><th>Last Updated</th></tr>
        </thead>
        <tbody>
          WORKER_ROW
        </tbody>
      </table>
    </section>
    <section>
      <br>
      <h3>Tuples in Messaging System</h3>
      <table class="table table-striped">
        <thead>
          <tr><th>Image Name</th><th>Amount</th></tr>
        </thead>
        <tbody>
          MSG_ROW
        </tbody>
      </table>
    </section>
        <section>
      <br>
      <h3>Containers Group</h3>
      <table class="table table-striped">
        <thead>
          <tr><th>Group</th><th>Address</th><th>Port</th><th>Status</th><th>Last Update</th></tr>
        </thead>
        <tbody>
          CONTAINER_ROW
        </tbody>
      </table>
    </section>
    <section>
      <br>
      <h3>Tuple Logs</h3>
      <table class="table table-striped">
        <thead>
          <tr><th>ID</th><th>Source</th><th>Image</th><th>Digest</th><th>priority</th><th>Last Update</th><th>Status</th></tr>
        </thead>
        <tbody>
          TUPLE_ROW
        </tbody>
      </table>
    </section>
    </div>
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>
  </body>
</html>
"""

    worker_row = ""
    for _, value in worker.items():
        worker_row += "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>".format(value['node_name'],
                                                                                                     value['node_addr'],
                                                                                                     value['docker'],
                                                                                                     str(value['load1']) + "|" + str(value['load5']) + "|" + str(value['load15']),
                                                                                                     value['last_upd'])


    msg_row = ""
    for key, value in msg.items():
        msg_row += "<tr><td>{0}</td><td>{1}</td></tr>".format(key, value)

    container_row = ""
    for key, value in containers.items():
        for item in value:
            container_row += "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>".format(item['c_name'],
                                                                                                            item['batch_addr'],
                                                                                                            item['batch_port'],
                                                                                                            item['batch_status'],
                                                                                                            item['last_upd'])

    tuple_row = ""
    for key, value in tuples.items():
        # <tr><td>id</td><td>source</td><td>image</td><td>digest</td><td>priority</td><td>last_update</td><td>status</td></tr>
        tuple_row += "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td></tr>".format(
            key, value['source'], value['c_name'], value['digest'], value['priority'], value['last_upd'], value['status']
        )

    html = html.replace("WORKER_ROW", worker_row)
    html = html.replace("MSG_ROW", msg_row)
    html = html.replace("CONTAINER_ROW", container_row)
    html = html.replace("TUPLE_ROW", tuple_row)

    return html
