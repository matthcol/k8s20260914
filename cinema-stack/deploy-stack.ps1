$NAMESPACE="cinema"
# TODO: check NS not empty and not existing

kubectl create ns $NAMESPACE
kubectl config set-context --current --namespace $NAMESPACE

# Config Maps
kubectl apply -f db-config.configmap.yml
kubectl apply -f db-init.configmap.yml

# Secrets
kubectl create secret generic db-secret --from-env-file db-secret

# Pods (sts and deploy)
kubectl apply -f db.statefulset.yml
kubectl apply -f api.deployment.yml

# Services

