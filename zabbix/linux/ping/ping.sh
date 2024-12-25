#!/bin/bash
ping -c4 $1 | grep received | awk '{print $4}'