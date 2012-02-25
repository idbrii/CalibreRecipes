#! /usr/bin/env python
# encoding: utf-8

from waflib import TaskGen
TaskGen.declare_chain(
    rule         = 'ebook-convert ${SRC} .epub --test -vv --debug-pipeline debug', 
    ext_in       = '.recipe', 
    ext_out      = '.epub'
)

top = '.'
out = 'build'

def configure(conf):
    pass

def build(bld):
    bld(source='Tested_11.recipe')
