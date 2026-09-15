$NAMESPACE="cinema"
kubectl create ns $NAMESPACE
kubectl config set-context --current --namespace $NAMESPACE

kubectl apply -f api.deployment.yml
