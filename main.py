import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

# Carregando o Conjunto de Dados
data = pd.read_csv('./kddcup.data_10_percent_corrected', header=None)

# Definindo as colunas
cols = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", "wrong_fragment",
        "urgent", "hot", "num_failed_logins", "logged_in", "num_compromised", "root_shell", "su_attempted",
        "num_root", "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login",
        "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate",
        "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
        "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
        "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate", "dst_host_rerror_rate",
        "dst_host_srv_rerror_rate", "target"]

data.columns = cols

# Convertendo o rótulo 'target' para binário: 0 = normal, 1 = ataque
data['binary_target'] = data['target'].apply(lambda x: 0 if x == 'normal.' else 1)

data['protocol_type'] = data['protocol_type'].astype('category').cat.codes
data['service'] = data['service'].astype('category').cat.codes
data['flag'] = data['flag'].astype('category').cat.codes

# Dividindo os dados em recursos (X) e rótulo (y)
X = data.drop(['target', 'binary_target'], axis=1)  # Features
y = data['binary_target']  # Rótulo (0 = normal, 1 = ataque)

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando o modelo de árvore de decisão com balanceamento de classes
model = DecisionTreeClassifier(random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# Fazendo previsões no conjunto de teste
y_pred = model.predict(X_test)

# Calculando a Matriz de Confusão
cm = confusion_matrix(y_test, y_pred)
print("Matriz de Confusão:")
print(cm)

# Exibindo o Relatório de Classificação
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred, target_names=['Normal', 'Ataque']))

# Filtro para dados apenas anômalos (ataques)
y_test_anomalia = y_test[y_test == 1]
y_pred_anomalia = y_pred[y_test == 1]

cm_anomalia = confusion_matrix(y_test_anomalia, y_pred_anomalia)
print("\nMatriz de Confusão (Somente Ataques):")
print(cm_anomalia)

print("\nRelatório de Classificação (Somente Ataques):")
print(classification_report(y_test_anomalia, y_pred_anomalia, target_names=['Normal', 'Ataque'], zero_division=1))
