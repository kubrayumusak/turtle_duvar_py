# Duvardan Kaçan Kaplumbağa (turtle_duvar_py)

Bu proje, ROS 2 Humble ortamında `turtlesim` simülatörünü kullanarak kaplumbağanın sınır duvarlarına çarpmadan yön değiştirmesini, anlık konumunun periyodik olarak loglanmasını ve hız/sınır değerlerinin parametrik olarak yönetilmesini sağlar.

---

## Proje Özellikleri

- **Paket Adı:** `turtle_duvar_py`
- **Abone (Subscriber):** `/turtle1/pose` konusuna abone olarak anlık $x$ ve $y$ koordinatlarını dinler.
- **Yayıncı (Publisher):** `/turtle1/cmd_vel` konusuna `geometry_msgs/msg/Twist` mesajları göndererek kaplumbağayı ileri sürer ve duvara yaklaştığında dönüş yaptırır.
- **Duvar Kontrol Mantığı:** Kaplumbağanın $x$ veya $y$ konumu `1.0` değerinden küçük veya `10.0` değerinden büyük olduğunda dönerek odanın içine geri yönelir.
- **Loglama:** Kaplumbağanın anlık konumu saniyede bir kez (`1.0 saniye` periyotla) `get_logger().info()` fonksiyonu ile terminale yazdırılır.
- **Bonus Özellik (ROS 2 Parametreleri):** Hızlar ve duvar sınırları kod içerisine sabitlenmemiş, ROS 2 parametresi olarak tanımlanmıştır:
  - `forward_speed` (Varsayılan: `2.0`)
  - `turn_speed` (Varsayılan: `1.5`)
  - `min_limit` (Varsayılan: `1.0`)
  - `max_limit` (Varsayılan: `10.0`)

---

## Kurulum ve Derleme

Çalışma alanınızın kök dizininde paketi derleyin:

```bash
cd ~/ros2_ws
colcon build --packages-select turtle_duvar_py
source install/setup.bash
