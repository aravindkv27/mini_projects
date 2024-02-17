import luigi

class HelloLuigi(luigi.Task):

    def output(slef):

        return luigi.LocalTarget('hello.txt')
    
    def run(self):

        with self.output().open('w') as outfile:
            outfile.write("Hello Aravind!")

