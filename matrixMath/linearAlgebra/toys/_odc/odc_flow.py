import numpy as np

print("Sup Pops!\n")

rev = 1000000


def sLabor(input):
    return input * .30
def sLOBs(input):
    return input * .32
def sProfit(input):
    return input * .05

def dLabor(input):
    return input * .38
def dLOBs(input):
    return input * .36
def dProfit(input):
    return input * -.1

def odcLabor(input):
    return input * .25
def odcLOBs(input):
    return input * .28
def odcProfit(input):
    return input * .18


print("standard:\n***************************\n",
      "standard labor:\n", sLabor(rev), "\nstandard LOBs:\n", sLOBs(rev),
       "\nstandard profit: \n", sProfit(rev), "\n")

print("disengaged:\n***************************\n",
      "disengaged labor:\n", dLabor(rev), "\ndisengaged LOBs:\n", dLOBs(rev),
       "\ndisengaged profit: \n", dProfit(rev), "\n")

print("with One Degree:\n***************************\n",
      "One Degree-enhanced labor:\n", odcLabor(rev), "\nOne Degree-enhanced LOBs:\n", odcLOBs(rev),
       "\nOne Degree-enhanced profit: \n", odcProfit(rev), "\n")




