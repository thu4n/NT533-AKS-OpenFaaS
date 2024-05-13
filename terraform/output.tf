output "client_certificate" {
  value     = azurerm_kubernetes_cluster.openfaas-aks-cluster.kube_config[0].client_certificate
  sensitive = true
}

output "kube_config" {
  value = azurerm_kubernetes_cluster.openfaas-aks-cluster.kube_config_raw

  sensitive = true
}

output "id" {
    value = azurerm_kubernetes_cluster.openfaas-aks-cluster.id
}

output "cluster_ca_certificate" {
  value = azurerm_kubernetes_cluster.openfaas-aks-cluster.kube_config.0.cluster_ca_certificate
}

output "host" {
  value = azurerm_kubernetes_cluster.openfaas-aks-cluster.kube_config.0.host
}