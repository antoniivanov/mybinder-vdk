from vdk.api.job_input import IJobInput


def run(job_input: IJobInput):
    res = job_input.execute_query("select 1")
    print(res)

    job_input.send_object_for_ingestion(payload={"id": "Hi"}, destination_table="hello_table")
    job_input.send_object_for_ingestion(payload={"id": "Hello"}, destination_table="hello_table")
    job_input.send_object_for_ingestion(payload={"id": "Hola"}, destination_table="hello_table")
