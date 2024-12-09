
#include <cmath>
#include <vector>
#include <iostream>

std::vector<double> maxwell_boltzmann(
    std::vector<double> v,
    double T,
    double m
) {
    const double k_B = 1.38e-23; // Constante de Boltzmann
    const double factor = std::pow((m / (2 * M_PI * k_B * T)), 3.0 / 2.0);
    std::vector<double> exponential;
    for (auto i: v) {
        exponential.push_back(
            std::exp(std::pow(i, 2) * -m / (2 * k_B * T))
        );
    }
    std::vector<double> result;
    for (auto i = 0; i < v.size(); i++) {
        result.push_back(
            4 * M_PI * std::pow(v[i], 2) * factor * exponential[i]
        );
    }
    return result;
}

int main(int argc, char const *argv[])
{
    std::vector<double> inicio;
    std::vector<double> resultado;
    for (auto i = 0; i <= 3000; i = i + 6) {
        inicio.push_back(i);
    }
    resultado = maxwell_boltzmann(
        inicio, 300, 1.67e-27
    );
    for (auto i: resultado) {
        std::cout << i << std::endl;
    }
    return 0;
}
