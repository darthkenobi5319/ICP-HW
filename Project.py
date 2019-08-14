# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 23:15:27 2019

@author: Harry Zhenghan Zhang
"""
import numpy as np
import pandas as pd 
import h5py
import os
from sklearn.model_selection import train_test_split
from keras.layers import Dense,Dropout
from keras.models import Sequential
from keras.regularizers import l2
from keras.models import load_model

# This function merges the dataframe of matchups with dataframes containing team info and conference info
# @param:   a dataframe of matchups containing teamID for both teams, ConfAbbrev
# @return:  a dataframe containing Team names and conference Names 
def joinByID(df):
    df_teams_temp = df_teams.drop(['FirstD1Season', 'LastD1Season'], axis=1)
    df_new = pd.merge(df,df_teams_temp ,how='left', left_on = 'WTeamID', right_on = 'TeamID')
    df_new = df_new.drop(['TeamID'], axis=1)
    df_new = df_new.rename(columns={"TeamName": "WinningTeamName"})
    df_new = pd.merge(df_new,df_teams_temp ,how='left', left_on = 'LTeamID', right_on = 'TeamID')
    df_new = df_new.drop(['TeamID'], axis=1)
    df_new = df_new.rename(columns={"TeamName": "LosingTeamName"})
    df_conf = pd.merge(df_team_conferences,df_conferences,how='left',left_on = 'ConfAbbrev', right_on = 'ConfAbbrev')
    df_conf = df_conf.drop(['ConfAbbrev'], axis=1)
    df_new = pd.merge(df_new,df_conf,how = 'left',left_on = ['Season','WTeamID'], right_on = ['Season','TeamID'])
    df_new = df_new.drop(['TeamID'], axis=1)
    df_new = df_new.rename(columns={"Description": "WinningTeamConference"}) 
    df_new = pd.merge(df_new,df_conf,how = 'left',left_on = ['Season','LTeamID'], right_on = ['Season','TeamID'])
    df_new = df_new.drop(['TeamID'], axis=1)
    df_new = df_new.rename(columns={"Description": "LosingTeamConference"})
    return df_new


# This function generates training data (X,y)
# The data used are regular season data (GLOBAL VARIABLE)
# @param:   
# @return:  tuple: (X,y) for training. need to manually use y.ravel() in training step.
def getTrainingData():
    df_match_data1 = df_reg_season_joined[['WFGM', 'WFGA', 'WFGM3', 'WFGA3', 'WFTM', 'WFTA', 'WOR', 'WDR',
       'WAst', 'WTO', 'WStl', 'WBlk', 'WPF', 'LFGM', 'LFGA', 'LFGM3', 'LFGA3',
       'LFTM', 'LFTA', 'LOR', 'LDR', 'LAst', 'LTO', 'LStl', 'LBlk', 'LPF']]
    df_match_data2 = df_reg_season_joined[[ 'LFGM', 'LFGA', 'LFGM3', 'LFGA3',
       'LFTM', 'LFTA', 'LOR', 'LDR', 'LAst', 'LTO', 'LStl', 'LBlk', 'LPF','WFGM', 'WFGA', 'WFGM3', 'WFGA3', 'WFTM', 'WFTA', 'WOR', 'WDR',
       'WAst', 'WTO', 'WStl', 'WBlk', 'WPF']]
    matrixData1 = np.matrix(df_match_data1)
    matrixData2 = np.matrix(df_match_data2)
    matrixData = np.concatenate((matrixData1, matrixData2), axis=0)
    #print(matrixData.shape)
    y = np.concatenate((np.ones((matrixData1.shape[0],1)),np.zeros((matrixData2.shape[0],1))),axis = 0)
    #print(y.shape)
    return matrixData,y




# This function creates a sequential model as described: two layers, 100 'relu' nodes with l2 regularization, 0.3 dropout.
# @param:  X: the matrix of all features
#          y: the binary variable of results(0/1)
#          path: to save the model, provide a string of absolute path
# @return: 
def createModel(X,y,path):
    #defifne a sequentail Model
    model = Sequential()
    #Hidden Layer-1
    model.add(Dense(100,activation='relu',input_dim = X.shape[1],kernel_regularizer=l2(0.01)))
    model.add(Dropout(0.3, noise_shape=None, seed=None))

    #Hidden Layer-2
    model.add(Dense(100,activation = 'relu',kernel_regularizer=l2(0.01)))
    model.add(Dropout(0.3, noise_shape=None, seed=None))

    #Output layer
    model.add(Dense(1,activation='sigmoid'))

    model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    print(model.summary())
    
    #train-test split
    x_train, x_test, y_train, y_test = train_test_split(X,y.ravel(),test_size=0.10)
    print('Shapes: x_train:',x_train.shape,'y_train:',y_train.shape,'x_test:',x_test.shape,'y_test',y_test.shape,sep= ' ')
    model_output = model.fit(x_train,y_train,epochs=100,batch_size=10,verbose=1,validation_data=(x_test,y_test),)
    print('Training Accuracy: ',np.mean(model_output.history['acc'] ))
    print('Validation Accuracy: ',np.mean(model_output.history['val_acc'] ))
     
    model.save(path)
    return 


# This function gets the average of every feature of every team
# @param:  
# @return: dataframe: Columns: Averages of each feature; Rows: team name
def getAverage():
    df_winning_teams = df_reg_season_joined[['WFGM', 'WFGA', 'WFGM3', 'WFGA3', 'WFTM', 'WFTA', 'WOR', 'WDR',
            'WAst', 'WTO', 'WStl', 'WBlk', 'WPF', 'WinningTeamName']]
    df_losing_teams = df_reg_season_joined[['LFGM', 'LFGA', 'LFGM3', 'LFGA3', 'LFTM', 'LFTA', 'LOR', 'LDR',
            'LAst', 'LTO', 'LStl', 'LBlk', 'LPF', 'LosingTeamName',]]
    columnDictWin = dict()
    columnDictLosing = dict()
    
    list1 = ['WFGM', 'WFGA', 'WFGM3', 'WFGA3', 'WFTM', 'WFTA', 'WOR', 'WDR',
            'WAst', 'WTO', 'WStl', 'WBlk', 'WPF', 'WinningTeamName']
    list2 = ['LFGM', 'LFGA', 'LFGM3', 'LFGA3', 'LFTM', 'LFTA', 'LOR', 'LDR',
            'LAst', 'LTO', 'LStl', 'LBlk', 'LPF', 'LosingTeamName',]
    list3 = ['FGM', 'FGA', 'FGM3', 'FGA3', 'FTM', 'FTA', 'OR', 'DR',
            'Ast', 'TO', 'Stl', 'Blk', 'PF', 'TeamName',]
    for i in range(len(list1)):
        columnDictWin[list1[i]] = list3[i]
        columnDictLosing[list2[i]] = list3[i]
        
    df_losing_teams = df_losing_teams.rename(columns= columnDictLosing)
    df_winning_teams = df_winning_teams.rename(columns= columnDictWin)
    df = pd.concat([df_winning_teams,df_losing_teams], axis = 0)
    df = df.groupby('TeamName').mean()
    return df

# This function generates a txt file containing all team names
# @param:  
# @return: 
def getTeamNames():
    fp = open(os.getcwd() + '/Stage2DataFiles/teamNames.txt','w')
    iterable = list(df_average.index)
    for i in iterable:
        print(i,file = fp)
    fp.close()
    return

# This function gets the average of every feature of two teams in one 'imaginary' matchup
# @param:  tuple(Team1,Team2) of both teams' name
# @return: a (1,26) maxtrix with both team information
def getInput(Team1,Team2):
    team1Avg = np.matrix(df_average.loc[Team1])
    team2Avg = np.matrix(df_average.loc[Team2])
    modelInput = np.concatenate((team1Avg ,team2Avg), axis = 1)
    return modelInput

# This function calls the user interface. It first trys to locate a model. If not found, it fits a model and store it locally as model.h5
# and then loads it
# Then it askes the user to input two team names, if entered correctly, it uses the model to predict and prints the result
# @param:  
# @return: 
def userInterface():
    path = os.getcwd() + '/Stage2DataFiles/Model.h5'

    try:
        model = load_model(path)
    except:
        data = getTrainingData()
        createModel(data[0],data[1],path)
        model = load_model(path)
    while True:
        Team1 = input('Please Enter the first team name: ')
        Team2 = input('Please Enter the second team name: ')
        try:
            model = load_model(path)
            y = model.predict(getInput(Team1,Team2))
        except:
            continue
        break
    print("Estimated sigmoid output: ",y[0][0])
    if y[0][0] >= 0.5:
        print(Team1, 'is predicted to win.',sep = ' ')
    elif y[0][0] <= 0.5:
        print(Team2, 'is predicted to win.',sep = ' ')
    else:
        print('An error has occurred!')
        
    return
        



if __name__ == '__main__':
    # Data Handling--Global Variables
    data_dir = os.getcwd() + '/Stage2DataFiles/'
    df_tour = pd.read_csv(data_dir + '/NCAATourneyDetailedResults.csv')
    df_reg_season = pd.read_csv(data_dir + "/RegularSeasonDetailedResults.csv")
    df_teams = pd.read_csv(data_dir + "/Teams.csv")
    df_tour_comp = pd.read_csv(data_dir + '/NCAATourneyCompactResults.csv')
    df_team_conferences = pd.read_csv(data_dir + '/TeamConferences.csv')
    df_conferences = pd.read_csv(data_dir + '/Conferences.csv')
    df_tour_joined = joinByID(df_tour)
    df_reg_season_joined = joinByID(df_reg_season)
    df_tour_comp_joined = joinByID(df_tour_comp)
    df_average = getAverage()
    
# =============================================================================
# =============================================================================
#   getTeamNames()
    userInterface()
    
    
    