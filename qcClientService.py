import json
import os
import sys
sys.path.insert(0, 'DataGeneratorServices')
import BarGraph
import HeatMap
import LineGraph
import PieChart
print("\nClient Service\n")


# Returns the number and list of clients from JSON file
def getClientsCode():
    clientsCodeAR = []
    clientsList = json.load(open('clientsDB.json'))
    clients = clientsList['clients-details']
    for client in clients:
        clientCode = client['onestone-client-']
        clientsCodeAR.append(clientCode)
    numClients = len(clientsCodeAR)
    return clientsCodeAR, numClients

def getNextClient(allClients):
    currentClient = ""

    if len(currentClient) == 0:
        currentClient = allClients[0]
    print(currentClient)

    currentClientIndex = allClients.index(currentClient)
    
    nextClientIndex = currentClientIndex + 1
    newCurrentClient = allClients[nextClientIndex]
    return newCurrentClient

def sendToDataGenerators(nextClient):
    print("Sending next client to generate Data")
    barGraphData = BarGraph.generateData(nextClient)
    heatMapData = HeatMap.generateData(nextClient)
    pieChartData = PieChart.generateData(nextClient)
    lineGraphData = LineGraph.generateData(nextClient)

    compiledData = [barGraphData,heatMapData,pieChartData,lineGraphData]
    return compiledData

def dataCollector(compiledData):
    print(compiledData)

def main():
    clientsList, numClients = getClientsCode()
    print(clientsList)
    returnedData = sendToDataGenerators(getNextClient(clientsList))
    print(returnedData)
    return returnedData

if __name__ == "__main__":
    main()