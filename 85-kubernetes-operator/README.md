# 85 - Custom Kubernetes Operator

This project demonstrates how to build a **Kubernetes Operator** using Python and the `kopf` (Kubernetes Operator Pythonic Framework) library.

Instead of deploying individual Pods, Deployments, and Services, companies often create "Custom Resource Definitions" (CRDs) that abstract these primitives into high-level concepts (e.g., `kind: Database`, or `kind: WebApp`). The Operator watches the Kubernetes API for these Custom Resources and automatically creates the underlying infrastructure.

## Key Concepts
- **Custom Resource Definition (CRD):** Extending the Kubernetes API to understand a new type of object (`EpycApp` in this demo).
- **Operator Pattern:** A software loop that watches for changes to your Custom Resource and reacts to them (create, update, delete).

## Running the Application

*You must have a running Kubernetes cluster (like Minikube or Docker Desktop K8s) and your `~/.kube/config` set up.*

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Apply the Custom Resource Definition (CRD) to your cluster:
   ```bash
   kubectl apply -f crd.yaml
   ```
3. Run the Operator locally (it will use your local kubeconfig to watch the cluster):
   ```bash
   kopf run operator.py --verbose
   ```
4. In another terminal, create an instance of your custom app:
   *(The second block in `crd.yaml` defines a test object `my-first-app`)*
   ```bash
   kubectl apply -f crd.yaml
   ```
5. Observe the Operator logs! It will intercept the creation event and print your logic.
