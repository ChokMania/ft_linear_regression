# ft_linear_regression [(sujet)](https://cdn.intra.42.fr/pdf/pdf/3505/ft_linear_regression.fr.pdf)

## Introduction

Le machine learning est un domaine croissant de l’informatique qui peut sembler un peu compliqué et réservé uniquement aux mathématiciens. Vous avez peut-être entendu parler des réseaux neuronaux ou des k-moyennes et n'avoir pas bien compris comment ils fonctionnent ou comment coder ces types de
algorithmes...
Mais ne vous inquiétez pas, nous allons en fait commencer avec un apprentissage simple, machine de base algorithme

## Objectifs

Le but de ce projet est de vous présenter le concept de base du machine learning. Pour ce projet, vous devrez créer un programme qui prédit le prix d’une voiture en utilisant un entrainement de [fonction linéaire](https://fr.wikipedia.org/wiki/Fonction_lin%C3%A9aire_(analyse)) avec un [algorithme de descente de gradient](https://fr.wikipedia.org/wiki/Algorithme_du_gradient).
Nous allons travailler sur un exemple précis pour le projet, mais une fois que vous aurez terminé, vous serez capable d’utiliser l’algorithme avec tout autre ensemble de données.

## Formules

$$estimatePrice(mileage) = \theta_{0} + (\theta_{1} * mileage)$$
$$tmp\theta_{0} = learningRate * \frac{1}{m} \sum_{i=0}^{m - 1} estimateP rice(mileage[i]) − price[i])$$
$$tmp\theta_{1} = learningRate * \frac{1}{m} \sum_{i=0}^{m - 1} estimateP rice(mileage[i]) − price[i]) * mileage[i]$$


## Le programme


