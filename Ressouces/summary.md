![](RackMultipart20211004-4-dhgwx7_html_37adf6fd2ee92099.jpg)

# RESUME DU LIVRE ImageDeblurring 2006

summary and computing

Nom | Intitulé du cours | Date

Ce document aborde des notions tels que : PSF, boundary conditions, and noise

Chapitre 1 : The Image deblurring Problem

Il s&#39;agit d&#39;une introduction aux concepts d&#39;images

Une image est composée de pixels auquel on assigne une intensité. Il y a plusieurs sources de flou dans les images:

- étalement de la lumière dans le système optique

- turbulence de l&#39;atmosphère

Que l&#39;image soit de bonne résolution ou pas, on a des images déformées lors de la prise de vues et on ne peut pas avoir l&#39;image originale parfaite par manque d&#39;informations. Pour commencer, on va essayer d&#39;enlever le flou

L&#39;élimination du flou d&#39;image (&quot;image deblurring&quot;) est un ensemble de méthodes dont l&#39;objectif est de récupérer l&#39;information cachée par le flou et de retrouver l&#39;image originale.

Pour cela, il est nécessaire de tenir compte de l&#39;influence de ce bruit sur l&#39;image à restaurer

Ce cours utilise Matlab un language qui offre assez d&#39;outils de traitement d&#39;images à travers STP et Ipt

Les représentations des images

Il y a une variété de formats de représentations des images. ON a des représentations à 2 ou 3 dimensions. Par exemple, le RGB stocke les images comme des intensités associés à une base (rouge , vert, bleu)

Le deblurring

On a des modèles de deblurring.

On suppose que le flou est une opération linéaire sur l&#39;ensemble des lignes et une autre opération linéaire sur l&#39;ensemble des colonnes

Ac.X.AcT = B

Cette approche permet de definir une image restaurée dite naive

Xnaive = Ac-1.B.Ar-T

Mais, cette restauration n&#39;est pas très bonne à cause d&#39;un bruit supplémentaire E qui est contenue dans l&#39;image à restaurer

B = Ac.X.Ar + E où E est une erreur matérielle

SVD

En vectorisant nos images, on peut obtenir une equation de la forme: Ax = b

Ax = b, x = vec(X),b=vec(B)

On applique la SVD à A afin de la décomposer dans une base de vecteurs singuliers. Il est à noter que le conditionnement de la matrice détermine fortement la domination de l&#39;erreur sur la solution. Si il est très grand, il y a beaucoup petites valeurs singulières très petites, ce qui rend la solution sensible aux perturbations.

Afin d&#39;éliminer ces composantes, on utilise la TSVD (SVD tronquée). Il s&#39;agit de tenir compte d&#39;un combre significatif de termes dans la décomposition de A en valeurs singulières

Chapitre 2

L&#39;objectif de ce chapitre est de montrer comment on manipule les images avec matlab.

On a diverses méthodes (stockage, opérations mathématiques,..) listées :

- Extraire des images : On a sur IPT, des images que l&#39;on peut extraire et utiliser (commande help imdemos/Contents)
- Lire des images : commande imread
- Visualiser des images : figure,imshow(image)
  - Parfois, il faut utiliser colorMap(). Sinon, on peut avoir un rendu innatendu surtout pour les images d&#39;intensité en niveaux de gris.
- Modifier une image : imwrite
- Faire des opérations arithmétiques sur une image :
  - Il faut transformer l&#39;image en array : commande double()
- Visualiser une image
  - Pour éviter les problèmes de « scalling » sur les images, fixer les valeurs que prends les composantes de la matrice : Imshow(Gd, [0, 255])
- Enregistrer une image : imwrite(mat2gray(X), &#39;Mylmage.jpg&#39;, &#39;Quality&#39;, 100)
-

Chapitre 3

Le chapitre 3 fournit une description mathématique du PSF et aborde aussi les conditions aux limites

Comme on l&#39;a expliqué en chapitre 1, il y a plusieurs sources au flou. Il s&#39;agit de problèmes - le flou vient de

- focus non parfait
- objet en mouvement ou cameraman en mouvement
- problèmes matériels
- effets optiques ou des effets du à l&#39;environnement.

Généralement, il y a des points très lumineux dans des images. Ce sont des points sources de lumières qu&#39;on appelle PSF.

Mathématiquement, il s&#39;agit d&#39;une matrice ayant la valeur 1 en un point et 0 partout ailleurs.

On a la forme du PSF dans plusieurs cas, que ce soit le « out of focus » ou celui de la turbulence atmosphérique

Il est à noter par ailleurs que la matrice PSF P est l&#39;image d&#39;un seul pixel blanc, et ses dimensions sont généralement beaucoup plus petits que ceux de B et X. Et dans le cas où il y a localement invariance du flou dans toutes les directions, alors le PSF contient toutes les informations sur le flou sur toute l&#39;image.

Le PSF détermine comment le flou a été construit pour avoir le maximum d&#39;informations sur l&#39;image, il f aut ajouter les conditions aux bords.

On a plusieurs types de condition aux bords :

- zero boundary condition : Aux bords de l&#39;image, il n&#39;y a rien que du noir
- periodic boundary condition : l&#39;image se répète dans toutes les directions
- reflexive boundary condition : L&#39;image se réflecte de part et d&#39;autres

Chapitre 4:

Le chapitre 4 introduit et decrit les opérations (FFT) avec les structures de matrices telles que les matrices circulantes, Toeplitz et Hankel, ainsi que les produits Kronecker et aussi des algorithmes rapides pour calculer la SVD ou la decomposiiton spectrale

En effet, lorsque le problème de restauration est spatialement invariant, on a des formes particulières de la matrice A selon les conditions aux bords du problème

En dimension 1

- zero boundary condition --\&gt; Toeplitz matrix
- periodic boundary condition --\&gt; matrice circulante
- reflexive Boundary Conditions--\&gt;Toeplitz-plus-Hankel matrix.

En dimension 2

- Zero Boundary Conditions--\&gt;BTTB
- Periodic Boundary Conditions--\&gt; BCCB matrix
- Reflexive Boundary Conditions--\&gt; BTTB + BTHB + BHTB + BHHB

Separable Two-Dimensional Blurs

- Zero Boundary Conditions--\&gt;Produit de Kronecker de matrices de Toeplitz
- Periodic Boundary Conditions--\&gt; Produit de Kronecker de matrices circulantes
- Reflexive Boundary Conditions--\&gt; Produit de Kronecker de matrices de la forme (Toeplitz-plus-Hankel)

Selon la structure du PSF, les conditions aux bords du problème et la structure de la matrice A, on dispose des algorithmes spécifiques pour trouver les valeurs propres de A ainsi que la solution naïve du problème de « deblurring »

- Decomposition spectrale : A = F\* F
- On peut obtenir cette décomposition à partie de la FFT, un algorithme en Nlog(N)
- Pour trouver les valeurs propres, on applique la fft à la première colonne de A : racine(N).F.a1 = vecteur contenant les valeurs propres de A
  - A partir du PSF, on a : S = fft2 ( circshift(P, 1 - center) );
- To compute the blurred image from the true image, use: B - real( ifft2 ( S .\* fft2 ( X ) ) ) ;
- To compute the naive solution from the blurred image, use: X = real( ifft2 (fft2 (B) ./ S ) ) ;

Pour le reste des structures, veuillez consulter le tableau suivant : Les détails ont dans le livre

|
 | BCCB matrix | **BTTB + BTHB + BHTB + BHHB Matrices** | **Kronecker Product Matrices** |
| --- | --- | --- | --- |
| Decomposition spectrale  | A = F\* F | A = CT.C | A = Ar.AC |
| Méthode pour l&#39;obtenir | FFT (complexité en Nlog(N)) | transformée cosine (DCT)  | A partir du PSF qu&#39;on décompose à l&#39;aide de la SVDOu soit on utilise kronDecomp de MAtlab |
| Pour trouver les valeurs propres | FFT appliqué à la première colonne de A | DCT appliqué à la première colonne de A | SVD appliqué à Ar et Ac |
| To compute the blurred image | FFT inverse | DCT inverse | Si Ar et Ac ne sont inversible, on résouds le système B = Ac.X.Ar&#39; |
| To compute the naive solution | Double FFT inverse | Double DCT inverse | Si Ar et Ac ne sont inversible, on résouds le système B = Ac.B.Ar&#39; |

# Chapitre 5 : SVD et analyse spectrale

## 1.Introduction au filtrage spectral

La méthode SVD est utilisée pour atténuer les effets du bruit en éliminant les petites valeurs singulières qui sont celles qui sont les plus affectées par le bruit. Ainsi, une façon d&#39;éliminer ces effets et d&#39;utiliser un paramètre de troncature k, cette méthode est appelée **SVD tronquée (TSVD).** La solution approchée est de la forme :

Xk =

Avec k\&lt;N où N est le nombre de toutes les valeurs singulières.

Plus le paramètre k est grand, plus le nombre de composantes est grand et plus le risque de prendre des composantes ternies par le bruit augmente. Puisque, ce sont les petites valeurs singulières qui sont influencées par le bruit, on introduit un facteur de filtrage qui est égale à 1 pour les grandes valeurs et 0 pour les petites de telle sorte à garder que les grandes valeurs.

Xfilt =

## 2.Incorporation des conditions de bord

Comme expliquer dans le chapitre 4, le choix des conditions de bord influe sur l&#39;image obtenue finalement.

## 3.Analyse SVD

Les composantes spectrales avec de plus grandes valeurs absolues contiennent des informations non altérées, les plus petites sont altérées par le bruit. En effet, pour choisir le paramètre de troncature qui permet d&#39;avoir la meilleure restitution, on doit déterminer la composante spectrale de transition c&#39;est-à-dire celle à partir de laquelle, les effets du bruit ne sont pas encore présents.

## 4. Base SVD pour la reconstruction d&#39;images

En faisant, la décomposition SVD d&#39;une matrice A, la base V des images ont des oscillations de plus en plus grandes, lorsque les valeurs singulières diminuent. De plus chaque vecteur de cette base doit respecter les conditions de bord imposées dans le problème. Ainsi, l&#39;image obtenue sera différente en fonction des conditions de bord auxquels sont soumis les vecteurs de base.

## 5. Bases obtenues par la DFT et la DCT

Les méthodes DFT et DCT donnent une factorisation immédiate de la matrice A (confère chapitre 4). L&#39;étude de la base issue de ces méthodes montre que pour toutes les types de conditions de bord, elles donnent de meilleurs résultats que la base issue de la SVD.

## 6.Condition discrète de Picard

La condition discrète de Picard stipule qu&#39;une condition nécessaire pour obtenir de bonnes solutions est que les coefficients issus de la décomposition SVD associé au problème décroissent plus rapidement à zéro que les valeurs singulières. En effet pour la plupart des problèmes de suppression du flou, les coefficients SVD obéissent à la condition discrète de Picard. Avec l&#39;ajout du bruit, les coefficients SVD décroissent en moyenne plus vite que les valeurs singulières et se stabilisent lorsque le bruit commence à dominer.

Chapitre 6

Le chapitre 6 montre l&#39;importance de la régularisation et présente les méthodes pour trouver les paramètres de régularisation.

![](RackMultipart20211004-4-dhgwx7_html_f82ac462376abbb8.gif) En effet, on peut faire de la restauration avec la SVD moyennant une fonction phi qui dépend de la valeur singulière. On a deux méthodes correspondantes respectivement à deux formes possibles pour phi.

- TSVD :

- Tikhonov :

La condition de choix des paramètres k ou alpha est de rendre|| b - Ax || 2 le plus petit que possible sans inclure les valeurs singulières relativement petites

La régularisation nécessite de trouver une balance entre erreur de régularisation et erreur de perturbation. Ce filtrage fréquentiel permet de supprimer le flou car le problème de suppression du flou satisfait la condition de Picard discrète.

Pour résoudre ce problème, on utilise le GCV (Validation croisée généralisée). Cette méthode de choix des paramètres détermine le paramètre alpha qui minimise la fonction GCV, où a est le paramètre de Tikhonov ou, en abusant de la notation, a = 1/ k, où k est le seuil TSVD.

G(α) =

On a par ailleurs le principe de discordance (The discrepancy principle) et le critère de la courbe en L

Ces trois méthodes ont soit des problèmes de disponibilité d&#39;information ou soit il sne convergent pas. Par exemple, GCV la norme de l&#39;erreur ne converge pas vers 0. De plus, son implémentation numérique est assez délicate car il s&#39;agit d&#39;une courbe en G dont il faut estimer le coin. Par ailleurs, le critère de la courbe en L, même si elles ont une implémentation numérique plus simple, posent des problèmes de condition aux limites mais aussi de convergence. Le principe de discordance (The discrepancy principle) converge mais les informations nécessaires sont indisponibles. De plus, les solutions ont une tendance à être trop lissées.

En résumé, aucune méthode de choix de paramètre n&#39;est parfaite, et choisir parmi les méthodes (principe de discordance, GCV, le critère de la courbe en L et d&#39;autres méthodes) dépendent des informations est disponible sur le problème.

#Le GCV pour la TSVD : G(k) =

#Le GCV pour Tikhonov : G(α) =

L&#39;implémentation de ces algorithmes est en Matlab (Matlab) et aussi en Python
