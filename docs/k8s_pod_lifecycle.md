# Kubernetes Pod Lifecycle

A Pod’s lifecycle includes:

1. Pending – accepted by kube-apiserver
2. Running – all containers are started
3. Succeeded – all containers terminated successfully
4. Failed – one or more containers failed
5. Unknown – state cannot be determined

Use `kubectl describe pod <name>` to investigate issues.

Monitor events and logs to track pod health.