import kopf
import logging

# We define what to do when a Custom Resource of type "EpycApp" is created
@kopf.on.create('epyc.io', 'v1', 'epycapps')
def create_fn(spec, name, namespace, logger, **kwargs):
    logger.info(f"Creating an EpycApp resource named {name} in {namespace}")
    image = spec.get('image', 'nginx:latest')
    replicas = spec.get('replicas', 1)
    
    logger.info(f"Specifications received: Image = {image}, Replicas = {replicas}")
    
    # In a real operator, here you would use the `kubernetes` python client payload
    # to create a Deployment, a Service, an Ingress, etc., based on this single CRD.
    return {
        'message': f"Successfully handled creation of {name}",
        'computed_replicas': replicas
    }

# We define what to do when it is updated
@kopf.on.update('epyc.io', 'v1', 'epycapps')
def update_fn(spec, name, namespace, logger, **kwargs):
    logger.info(f"Updating EpycApp resource {name}")
    replicas = spec.get('replicas', 1)
    logger.info(f"New Replicas = {replicas}")

# We define what to do when it is deleted
@kopf.on.delete('epyc.io', 'v1', 'epycapps')
def delete_fn(name, logger, **kwargs):
    logger.info(f"Deleting EpycApp resource {name}")
    logger.info("Cleaning up associated Deployments and Services...")
