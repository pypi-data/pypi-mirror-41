#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool

inputs:
  out_stdout:
    type: string
  msg:
    type: string
    inputBinding:
      position: 1

outputs:
  out_stdout:
    type: stdout

stdout: $(inputs.out_stdout)

baseCommand: ["echo"]
