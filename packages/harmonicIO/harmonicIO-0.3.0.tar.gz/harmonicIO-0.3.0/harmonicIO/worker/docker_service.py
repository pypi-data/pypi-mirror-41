from .docker_master import DockerMaster


class DockerService(object):
    __docker_master = None

    @staticmethod
    def init():
        DockerService.__docker_master = DockerMaster()

    @staticmethod
    def create_container(container_name):
        return DockerService.__docker_master.run_container(container_name)

    @staticmethod
    def get_containers_status():
        return DockerService.__docker_master.get_containers_status()
