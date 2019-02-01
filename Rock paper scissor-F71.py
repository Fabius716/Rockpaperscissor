
import numpy.random as nr
i=input("play\n")
n=nr.randint(3)
g=["r","p","s"]
"""
print(n)
"""
print(g[n])

if i == "r" and n==2:
	print("win")
if i == "r" and n==1:
	print("loss")
if i == "r" and n==0:
	print("tie")

if i == "p" and n==2:
	print("loss")
if i == "p" and n==1:
	print("tie")
if i == "p" and n==0:
	print("win")

if i == "s" and n==2:
	print("tie")
if i == "s" and n==1:
	print("win")
if i == "s" and n==0:
	print("loss")
