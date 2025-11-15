import numpy as np
import os
from scipy.signal import convolve2d
from skimage import io, img_as_float, color

# =============================
# Normalização para salvar PNG
# =============================
def normalize_to_uint8(img):
    img = img - img.min()
    if img.max() > 0:
        img = img / img.max()
    return (img * 255).astype(np.uint8)


# =============================
# Definição dos filtros
# =============================
def get_filters():
    h1 = np.array([
        [0, 0, -1, 0, 0],
        [0, -1, -2, -1, 0],
        [-1, -2, 16, -2, -1],
        [0, -1, -2, -1, 0],
        [0, 0, -1, 0, 0]
    ])

    h2 = (1/256) * np.array([
        [1, 4, 6, 4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1, 4, 6, 4, 1]
    ])

    h3 = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])

    h4 = np.array([
        [-1, -2, -1],
        [0,  0,  0],
        [1,  2,  1]
    ])

    h5 = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ])

    h6 = (1/9) * np.ones((3, 3))

    h7 = np.array([
        [-1, -1, 2],
        [-1,  2, -1],
        [2, -1, -1]
    ])

    h8 = np.array([
        [2, -1, -1],
        [-1, 2, -1],
        [-1, -1, 2]
    ])

    h9 = (1/9) * np.eye(9)

    h10 = (1/8) * np.array([
        [-1, -1, -1, -1, -1],
        [-1,  2,  2,  2, -1],
        [-1,  2,  8,  2, -1],
        [-1,  2,  2,  2, -1],
        [-1, -1, -1, -1, -1]
    ])

    h11 = np.array([
        [-1, -1, 0],
        [-1,  0, 1],
        [0, 1, 1]
    ])

    filters = {
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
        "h9": h9,
        "h10": h10,
        "h11": h11,
        "h3_plus_h4": h3 + h4
    }

    return filters


# =============================
# Aplica filtro (gray ou RGB)
# =============================

def apply_filter(img, kernel):

    # GRAYSCALE
    if len(img.shape) == 2:
        return convolve2d(img, kernel, mode='same', boundary='symm')

    # COLORIDA (RGB)
    result = np.zeros_like(img)
    for c in range(3):  # R=0, G=1, B=2
        result[:, :, c] = convolve2d(img[:, :, c], kernel, mode='same', boundary='symm')

    return result


# =============================
# Processo de várias imagens
# =============================
def process_folder(input_folder="input", output_folder="output"):
    filters = get_filters()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = [f for f in os.listdir(input_folder)
              if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp"))]

    if not images:
        print("Nenhuma imagem encontrada.")
        return

    for img_name in images:
        print(f"\nProcessando {img_name}...")

        img_path = os.path.join(input_folder, img_name)
        img = io.imread(img_path)
        img = img_as_float(img)

        # Pasta para resultados desta imagem
        img_dir = os.path.join(output_folder, img_name.split(".")[0])
        os.makedirs(img_dir, exist_ok=True)

        # Aplicação dos filtros
        for name, kernel in filters.items():
            print(f"  - Aplicando {name}...")

            filtered = apply_filter(img, kernel)

            # Normalização:
            if filtered.ndim == 2:  # gray
                filtered_uint8 = normalize_to_uint8(filtered)
            else:  # RGB
                filtered_uint8 = np.zeros_like(filtered, dtype=np.uint8)
                for c in range(3):
                    filtered_uint8[:, :, c] = normalize_to_uint8(filtered[:, :, c])

            # Salvar arquivo
            save_path = os.path.join(img_dir, f"{name}.png")
            io.imsave(save_path, filtered_uint8)

    print("\nProcessamento concluído!")


# =============================
# Execução
# =============================
if __name__ == "__main__":
    process_folder("input", "output")
