## Kebernetes
В директории хранятся манифесты для kubernetes

### Ingress
В качестве ingress контроллера в кластере используется NGINX Ingress Controller с типом NodePort. [Установка](https://kubernetes.github.io/ingress-nginx/deploy/#bare-metal-clusters)

Кластер развернут с использованием подхода, описанным [здесь](https://kubernetes.github.io/ingress-nginx/deploy/baremetal/#using-a-self-provisioned-edge). В качестве промежуточного узла используется haproxy, в конец /etc/haproxy/haproxy.cfg нужно добавить:
```
frontend front_nginx_ingress_controller
        bind *:80
        default_backend nginx_ingress_controller_service

backend nginx_ingress_controller_service
        balance roundrobin
        server node-1 <node 1 ip>:<ingress controller port> check port <ingress controller port>
        server node-2 <node 2 ip>:<ingress controller port> check port <ingress controller port>
```
Также для большей отказоустойчивости следует увеличить количество подов для контроллера:
```
kubectl scale deployment --namespace ingress-nginx ingress-nginx-controller --replicas=2
```

### Режим тестирования
Для использования режима тестирования в кластере нужно установить значение переменной MOCK_WEATHER_API_FOR_TESTS=1 в weather-deployment:
```
kubectl set env deployment/weather-deployment MOCK_WEATHER_API_FOR_TESTS=1
```
