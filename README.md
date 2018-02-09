# DESCRIPTION

We develop a Python source code of Expectation-Maximization (EM)-based algorithms for estimating error covariances in Lorenz-63 state-space models. We investigate to create stochastic (appximation) EM algorithms using Conditional Particle Filtering-Backward Simulation (CPF-BS-S(A)EM). The approach is compared to other EM methods using Extended Kalman smoother (EKS-EM), Ensemble Kalman smoother (EnKS-EM), a standard Particle smoother (PF-BS-S(A)EM) and Conditional particle filtering-Ancestor sampling smoother (CPF-AS-S(A)EM). We show their performances in terms of estimating log likelihood function, errors covariances. We also compare the reconstruction quality (RMSE, coverage probability) between CPF-BS and CPF-AS smoothers.

This Python library was contructed based on the CEDA library, which is available on https://github.com/ptandeo/CEDA. A main testing file is named as *test_Lorenz63_EM.ipynb*. 

# CITING
Article *An efficient particle-based method for maximum likelihood parameter estimates in nonlinear state-space models* of authors "T.T.T. Chau, P. Ailliot, V. Monbet, P. Tandeo", submitted to the Quarterly Journal of the Royal Meteorological Society.

# CONTACT:
Authors: Thi Tuyet Trang Chau (thi-tuyet-trang.chau@univ-rennes1.fr) and Pierre Tandeo (pierre.tandeo@telecom-bretagne.fr)
