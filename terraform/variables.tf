variable "resource_group_name" {
  description = "The name of Azure resource group"
  default = ""
  type = string
}

variable "location" {
  description = "The location of Azure"
  default = ""
  type = string
}

variable "aks_name" {
  description = "The name of AKS cluster"
  default = ""
  type = string
}

variable "aks-dns-prefix" {
  description = "The DNS prefix of AKS cluster"
  default = ""
  type = string
}

variable "aks-agentpool" {
  description = "The Agentpool of AKS cluster"
  default = ""
  type = string
}