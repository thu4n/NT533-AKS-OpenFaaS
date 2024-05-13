resource "azurerm_resource_group" "openfaas-group" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_kubernetes_cluster" "openfaas-aks-cluster" {
  name                = var.aks_name
  location            = azurerm_resource_group.openfaas-group.location
  resource_group_name = azurerm_resource_group.openfaas-group.name
  dns_prefix = var.aks-dns-prefix

  default_node_pool {
    name       = var.aks-agentpool
    node_count = 1
    vm_size    = "Standard_B2s"
  }

  identity {
    type = "SystemAssigned"
  }
}