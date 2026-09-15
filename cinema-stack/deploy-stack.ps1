$NAMESPACE="cinema"
# TODO: check NS not empty and not existing

kubectl create ns $NAMESPACE
kubectl config set-context --current --namespace $NAMESPACE


kubectl apply -f db-config.configmap.yml
kubectl apply -f db-init.configmap.yml

kubectl apply -f db.statefulset.yml
kubectl apply -f api.deployment.yml

