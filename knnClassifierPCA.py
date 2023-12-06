import numpy
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def knn_classifier_pca():
    file_x = 'data/features_raw.dat'
    file_y = 'data/label_class_0.dat'
    
    X = numpy.genfromtxt(file_x, delimiter=' ')
    y = numpy.genfromtxt(file_y, delimiter=' ')
    
    # Split the data into training/testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
           
    # PCA to select features
    pca = PCA(n_components=20, svd_solver='full')
    pca.fit(X)
    X = pca.transform(X)
       	
    # KNN classsifier
    clf = KNeighborsClassifier(n_neighbors=9)
    trained_model=clf.fit(X_train,y_train)
    trained_model.fit(X_train,y_train )
    
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    cm = confusion_matrix(y_test, y_predict)
    print(cm)
    
    print("Accuracy score of valence test KNN-PCA")
    
    print(accuracy_score(y_test, y_predict)*100)
    
    
    ########################################################################
    file_x = 'data/features_raw.dat'
    file_y = 'data/label_class_1.dat'
    
    X = numpy.genfromtxt(file_x, delimiter=' ')
    y = numpy.genfromtxt(file_y, delimiter=' ')
    
    # Split the data into training/testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
        
    # PCA to select features
    pca = PCA(n_components=20, svd_solver='full')
    pca.fit(X)
    X = pca.transform(X)
        	
    # KNN classsifier
    clf = KNeighborsClassifier(n_neighbors=9)
    trained_model=clf.fit(X_train,y_train)
    trained_model.fit(X_train,y_train )
    
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    cm = confusion_matrix(y_test, y_predict)
    print(cm)
    
    print("Accuracy score of Arousal test KNN-PCA")
    print(accuracy_score(y_test, y_predict)*100)
        
    ##########################################################################33
    file_x = 'data/features_raw.dat'
    file_y = 'data/label_class_2.dat'
    
    X = numpy.genfromtxt(file_x, delimiter=' ')
    y = numpy.genfromtxt(file_y, delimiter=' ')
    
    # Split the data into training/testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
       
    # PCA to select features
    pca = PCA(n_components=20, svd_solver='full')
    pca.fit(X)
    X = pca.transform(X)
    #explained_variance=pca.explained_variance_ratio_
       	
    # KNN classsifier
    clf = KNeighborsClassifier(n_neighbors=9)
    trained_model=clf.fit(X_train,y_train)
    trained_model.fit(X_train,y_train )
    
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    cm = confusion_matrix(y_test, y_predict)
    print(cm)
    
    print("Accuracy score of Dominance test KNN-PCA")
    print(accuracy_score(y_test, y_predict)*100)
    
    
    ######################################################################
    file_x = 'data/features_raw.dat'
    file_y = 'data/label_class_3.dat'
    
    X = numpy.genfromtxt(file_x, delimiter=' ')
    y = numpy.genfromtxt(file_y, delimiter=' ')
    
    # Split the data into training/testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
       
    # PCA to select features
    pca = PCA(n_components=20, svd_solver='full')
    pca.fit(X)
    X = pca.transform(X)
    #explained_variance=pca.explained_variance_ratio_
       	
    # KNN classsifier
    clf = KNeighborsClassifier(n_neighbors=9)
    trained_model=clf.fit(X_train,y_train)
    trained_model.fit(X_train,y_train )
    
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    cm = confusion_matrix(y_test, y_predict)
    print(cm)
    
    print("Accuracy score of Liking test KNN-PCA")
    print(accuracy_score(y_test, y_predict)*100)
    
    
    
if __name__ == '__main__':
    knn_classifier_pca()