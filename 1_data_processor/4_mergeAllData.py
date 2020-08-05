import pandas as pd
import numpy as np

from dataHandler import *


def mergeAllChatterBotData():
    csv_whatsapp = "{}/{}_FINAL.csv".format(output_dir, SocialNetwork.WhatsApp.name)
    csv_hangout = "{}/{}_FINAL.csv".format(output_dir, SocialNetwork.Hangout.name)
    csv_facebook = "{}/{}_FINAL.csv".format(output_dir, SocialNetwork.Facebook.name)

    df_all = pd.read_csv(csv_whatsapp)
    df_all.replace(np.NaN, ' ', inplace=True)

    df_hangout = pd.read_csv(csv_hangout)
    df_hangout.replace(np.NaN, ' ', inplace=True)
    df_all = df_all.append(df_hangout)

    df_facebook = pd.read_csv(csv_facebook)
    df_facebook.replace(np.NaN, ' ', inplace=True)
    df_all = df_all.append(df_facebook)

    return df_all


if __name__ == '__main__':
    combinedDF = mergeAllChatterBotData()
    combinedDF.to_csv("{}/ALL_chatterbot_FINAL.csv".format(output_dir))
    print("DONE!!!")
