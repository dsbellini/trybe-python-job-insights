from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    original_list = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    translated_job = {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee",
    }
    assert original_list[0] == translated_job
