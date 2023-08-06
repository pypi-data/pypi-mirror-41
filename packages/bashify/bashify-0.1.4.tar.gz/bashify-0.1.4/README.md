Use:

	from bashify import bashify

    lines = ["test=$(service mongod status)", "echo 'test'", "echo $test"]
    name = "test"

    b = bashify(name, lines)
    b.runExecutable()

    b2 = bashify()

    b2.printBashFile(name, lines)
    b2.makeExecutable(name)
    b2.runExecutable(name)


Allows you to create and execute shell scripts with a list of lines to add to the shell script. Can make intefacing with a system feel more natural and requires less knowledge of the nuances of python's system interfaces. Output is returned to the calling shell, so, you will need to echo your output to a file and read from there. Support for this will be added in future versions. 

https://pypi.org/project/bashify/

https://github.com/UniWrighte/bashify