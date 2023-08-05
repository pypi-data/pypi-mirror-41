.. note::
    :class: sphx-glr-download-link-note

    Click :ref:`here <sphx_glr_download_gallery_optimization_framework_example.py>` to download the full example code
.. rst-class:: sphx-glr-example-title

.. _sphx_glr_gallery_optimization_framework_example.py:


A PyAI (optimization framework) demo.



.. code-block:: python

    import math
    import numpy as np

    # CONFIG ######################################################################

    objective_func = "sphere"
    optimizer_choice = "saes"

    # MAIN ########################################################################

    def main():
        """
        A PyAI (optimization framework) demo.
        """

        # SETUP OBJECTIVE FUNCTION ############################

        if objective_func == "sphere":
            # Sphere ##########################
            from ailib.optimization.function.sphere import Function
            #f = Function(1)
            f = Function(2)
            #f = Function(10)

        elif objective_func == "noised_sphere":
            # Noised sphere ###################
            from ailib.optimization.function.noised_sphere import Function
            #f = Function(1)
            f = Function(2)

        elif objective_func == "sin1":
            # Sinusoid functions ##############
            from ailib.optimization.function.sin1 import Function
            f = Function()

        elif objective_func == "sin2":
            # Sinusoid functions ##############
            from ailib.optimization.function.sin2 import Function
            f = Function()

        elif objective_func == "sin3":
            # Sinusoid functions ##############
            from ailib.optimization.function.sin3 import Function
            f = Function()

        elif objective_func == "yahoo":
            # Yahoo function ##################
            from ailib.optimization.function.yahoo import Function
            f = Function()

        elif objective_func == "deg_2_poly":
            # Degree 2 polynomial function ####
            from ailib.optimization.function.degree_2_polynomial import Function
            f = Function(np.array([6.,2.]), np.array([1.,2.]), 1., 2)

        else:
            raise Exception("Wrong objective_func value.")

        # Plot ########
        #f.plot()


        # OPTIMIZER ###########################################

        if optimizer_choice == "naive":
            # Naive Minimizer #################
            from ailib.optimization.optimizer.naive import Optimizer
            optimizer = Optimizer()
            best_x = optimizer.optimize(f, num_samples=300)

        elif optimizer_choice == "gradient":
            # Gradient descent ################
            from ailib.optimization.optimizer.gradient import Optimizer
            optimizer = Optimizer()
            f.delta = 0.01
            best_x = optimizer.optimize(f, num_iterations=30)

        elif optimizer_choice == "saes":
            # SAES ############################
            from ailib.optimization.optimizer.saes_hgb import Optimizer
            optimizer = Optimizer(x_init=np.ones(f.ndim), num_evals_func=lambda gen_index: math.floor(10. * pow(gen_index, 0.5)))
            optimizer = Optimizer(x_init=np.ones(f.ndim))
            best_x = optimizer.optimize(f, num_gen=50)

        elif optimizer_choice == "cutting_plane":
            # Cutting plane ###################
            from ailib.optimization.optimizer.cutting_plane import Optimizer
            optimizer = Optimizer()

            #best_x = optimizer.optimize(f, num_iterations=7)   # sphere with 1 dimension
            #best_x = optimizer.optimize(f, num_iterations=15) # sphere with 2 dimensions
            #best_x = optimizer.optimize(f, num_iterations=100) # sphere with 10 dimensions

            #best_x = optimizer.optimize(f, parallel="linear", num_iterations=7)   # sphere with 1 dimension
            #best_x = optimizer.optimize(f, parallel="linear", num_iterations=100)   # sphere with 10 dimension

            #best_x = optimizer.optimize(f, parallel="gaussian", num_iterations=7)   # sphere with 1 dimension
            #best_x = optimizer.optimize(f, parallel="gaussian", num_iterations=100)   # sphere with 10 dimension

            best_x = optimizer.optimize(f, num_iterations=15) # sphere with 2 dimensions

        elif optimizer_choice == "eda":
            # EDA #############################
            #from ailib.optimization.optimizer.eda import Optimizer
            pass

        else:
            raise Exception("Wrong optimizer_choice value.")

        print("Best sample: f(", best_x, ") = ", f(best_x))

    if __name__ == '__main__':
        main()


**Total running time of the script:** ( 0 minutes  0.000 seconds)


.. _sphx_glr_download_gallery_optimization_framework_example.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download

     :download:`Download Python source code: optimization_framework_example.py <optimization_framework_example.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: optimization_framework_example.ipynb <optimization_framework_example.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.readthedocs.io>`_
