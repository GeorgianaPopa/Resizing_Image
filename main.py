import cv2

# Încărcați imaginea
imagine = cv2.imread('C:/Users/georg/Desktop/opencv_prj/Doggy.jpg')

# Verificați dacă imaginea a fost încărcată corect
if imagine is None:
    print('Eroare: Imaginea nu a putut fi încărcată.')
else:
    # Specificați noile dimensiuni pentru redimensionare
    noua_latime = 300
    noua_inaltime = 300

    # Redimensionați imaginea
    imagine_redimensionata = cv2.resize(imagine, (noua_latime, noua_inaltime))

    # Afișați imaginea redimensionată într-o fereastră
    cv2.imshow('Imagine Redimensionată', imagine_redimensionata)

    # Așteptați apăsarea unei taste înainte de a închide fereastra
    cv2.waitKey(0)

    # Închideți toate ferestrele deschise
    cv2.destroyAllWindows()
