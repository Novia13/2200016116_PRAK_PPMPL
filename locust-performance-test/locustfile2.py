from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Tunggu antara 1 hingga 5 detik sebelum request selanjutnya

    @task
    def get_users(self):
        self.client.get("/users")

    @task
    def get_user_by_id(self):
        user_id = 1  # Contoh user ID
        self.client.get(f"/users/{user_id}")

    @task
    def create_user(self):
        # Mengirim request POST untuk membuat pengguna baru
        self.client.post("/users", json={"name": "User Baru", "email": "userbaru@example.com"})

    @task
    def update_user(self):
        user_id = 1  # Contoh user ID
        # Mengirim request PUT untuk memperbarui data pengguna
        self.client.put(f"/users/{user_id}", json={"name": "User Diupdate", "email": "userdiupdate@example.com"})

    @task
    def delete_user(self):
        user_id = 1  # Contoh user ID
        # Mengirim request DELETE untuk menghapus pengguna
        self.client.delete(f"/users/{user_id}")
