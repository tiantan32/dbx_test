from dbx_test.common import Job
from dbx_test.custom_utils import custom_func

class SampleJob(Job):

    def launch(self):
        self.logger.info("Launching sample job")

        listing = self.dbutils.fs.ls("dbfs:/")

        for l in listing:
            self.logger.info(f"DBFS directory: {l}")

        df = self.spark.range(0, 1000)

        df.write.format(self.conf["output_format"]).mode("overwrite").save(
            self.conf["output_path"]
        )

        self.logger.info("Sample job finished!")


if __name__ == "__main__":
    custom_result = custom_func()
    print('result from custom_result: ', custom_result)
    job = SampleJob()
    job.launch()
    
