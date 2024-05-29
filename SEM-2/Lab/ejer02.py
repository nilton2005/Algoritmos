# Función de Torres de Hanoi
def towersOfHanoi(numberOfDisks, src=1, dest=3, tmp=2):
    if numberOfDisks:
        towersOfHanoi(numberOfDisks-1, src=src, dest=tmp, tmp=dest)
        print("Mover disco %d desde la estaca %d a la estaca %d" % (numberOfDisks, src, dest))
        towersOfHanoi(numberOfDisks-1, src=tmp, dest=dest, tmp=src)

if __name__ == "__main__":
    # Ejecutar
    towersOfHanoi(numberOfDisks=3)
