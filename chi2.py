"""from sklearn.feature_selection import chi2
temp= {}
for key in df_app.columns:
    if key  != "TARGET": 
        if df_app[key].dtype=='float'or  df_app[key].dtype=='int'  :
            
            temp2 = df_app[[key,"TARGET"]].dropna()
            chi_val, p_val =chi2(np.absolute(temp2[key].values.reshape(-1,1)),temp2["TARGET"])
            temp[key] =[chi_val[0],p_val[0]]
     
features_score_chi2= pd.DataFrame(data=temp,index=["CHI-2","P-Value"]).T
features_score_chi2.sort_values(by="CHI-2",ascending=False,inplace=True)

        
            #features_score_chi2= pd.DataFrame(data=temp,index=["CHI-SQUARE"])

"""
"""#features_score_chi2["CHI-2"].plot(kind='barh',figsize=(10,20),yticks=[]),plt.title('CHI-2')
plt.subplot(121),features_score_chi2["CHI-2"].plot(kind='barh',figsize=(10,20)), plt.title('CHI-2')
plt.subplot(122),features_score_chi2["P-Value"].plot(kind='barh',figsize=(10,20),yticks=[]),plt.title('Valor P')

plt.yticks([])
plt.show()   """

"""grouped_test = df_app.groupby(["TARGET"])
plt.subplot(221),
grouped_test.get_group(0)["DAYS_EMPLOYED"].plot(kind='hist',alpha=0.5,density=True,figsize=(10,10))
grouped_test.get_group(1)["DAYS_EMPLOYED"].plot(kind='hist',alpha=0.5,density=True,figsize=(10,10))
plt.title("DAYS_EMPLOYED")

plt.subplot(222)
grouped_test.get_group(0)["AMT_GOODS_PRICE"].plot(kind='hist',alpha=0.5,density=True,figsize=(10,10))
grouped_test.get_group(1)["AMT_GOODS_PRICE"].plot(kind='hist',alpha=0.5,density=True,figsize=(10,10))
plt.title("AMT_GOODS_PRICE")

plt.subplot(223)

grouped_test.get_group(0)["AMT_INCOME_TOTAL"].plot(kind='hist',alpha=0.5,density=True,figsize=(10,10))
grouped_test.get_group(1)["AMT_INCOME_TOTAL"].plot(kind='hist',alpha=0.5,density=True,figsize=(10,10))
plt.title("AMT_INCOME_TOTAL")
"""