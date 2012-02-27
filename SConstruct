#! /usr/bin/env python
# encoding: utf-8

# Define Rules
def add_custom_builder(env):
    # filename transformation
    suffix = '.epub'
    src_suffix = '.recipe'

    # define the build method
    rule = 'ebook-convert $SOURCE .epub --test -vv --debug-pipeline debug'
    bld = Builder(action = rule,
                  suffix = suffix,
                  src_suffix = src_suffix)
    env.Append(BUILDERS = {'Book' : bld})

    # define the targets (to autobuild by passing output filename)
    for target in Glob('*' + src_suffix):
        env.Book(target)

# Create
env = Environment()
add_custom_builder(env)

# Define Explicit Targets
Default(env.Book('Tested.recipe'))
