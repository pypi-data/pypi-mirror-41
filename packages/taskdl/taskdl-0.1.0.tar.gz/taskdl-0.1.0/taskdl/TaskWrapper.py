import subprocess
import json


class TaskWrapper(object):

    images = {
        'tensorflow': 'tensorflow/tensorflow:1.12.0-gpu-py3'
    }

    def __init__(self, dataset_id, workspace='/tmp', file_delimiter='/', env='us'):
        self.dataset_id = dataset_id
        self.workspace = workspace
        self.file_delimiter = file_delimiter
        self.env = env

    def __upload_python_file(self, python_path):
        result = subprocess.check_output(['lo', 'files-upload', python_path, self.dataset_id, '--overwrite'])
        file_id = result.split(' ')[-1]
        return file_id.strip()

    def __construct_inputs(self, python_path, file_datasets=None):
        file_name = python_path.split(self.file_delimiter)[-1]
        file_id = self.__upload_python_file(python_path)
        inputs = [{
            "path": '%s/%s' % (self.workspace, file_name),
            "url": "https://api.%s.lifeomic.com/v1/files/%s" % (self.env, file_id),
            "type": "FILE"
        }]
        if file_datasets:
            for file_d in file_datasets:
                data_type = "DIRECTORY" if file_d.is_directory else "FILE"
                inputs.append({
                    "path": '%s/%s' % (self.workspace, file_d.file_name),
                    "url": "https://api.%s.lifeomic.com/v1/files/%s" % (self.env, file_d.file_id),
                    "type": data_type
                })
        return inputs

    def construct_body(self, task_name, inputs, image, output_path='model_data.zip'):
        return {
            "name": task_name,
            "datasetId": self.dataset_id,
            "inputs": inputs,
            "outputs": [
                {
                    "path": '%s/%s' % (self.workspace, output_path),
                    "url": "https://api.%s.lifeomic.com/v1/projects/%s" % (self.env, self.dataset_id),
                    "type": "FILE"
                }
            ],
            "resources": {
                "gpu_cores": 1
            },
            "executors": [
                {
                    "workdir": self.workspace,
                    "image": image,
                    "command": [
                        "python",
                        inputs[0]['path']
                    ],
                    "stderr": "%s/test/stderr.txt" % self.workspace,
                    "stdout": "%s/test/stdout.txt" % self.workspace
                }
            ]
        }

    def run_task(self, python_path, image='tensorflow', task_name='Deep Learning Task', file_datasets=None):
        image = self.images[image]
        inputs = self.__construct_inputs(python_path, file_datasets)
        body = self.construct_body(task_name, inputs, image)
        print(json.dumps(body))


class FileDataset(object):

    def __init__(self, file_id, file_name, is_directory=False):
        if not file_id or not file_name:
            raise RuntimeError("File Id and file name must be implemented")
        self.file_id = file_id
        self.file_name = file_name
        self.is_directory = is_directory


