# Test file for the plots.py plot_data function
import pytest
import matplotlib.pyplot as plt

from pkmodel.plot_function import plot_data

#Define a fixture to set up sample data for the following tests


def test_no_error_raised():
    #Test the plot runs without an error"
    
    t = range(0, 10)
    qp = range(10, 20)
    qc = range(20, 30)
   
    #Run the plot function, test no exceptions (errors) raised
    try: 
        fig = plot_data(t, qp, qc)  
    except Exception as e:
        pytest.fail(f"plot_data raised an exception: {e}")


def test_figure_returned():
    #Test plot_data produces a figure

    t = range(0, 10)
    qp = range(10, 20)
    qc = range(20, 30)

    #Run the plot function and assert if return is a figure object
    fig = plot_data(t, qp, qc)
    assert isinstance(fig, plt.Figure), "plot_data did not return a Figure object"


    
def test_labels_correct():
    #Test the figure axes are correctly labelled

    t = range(0, 10)
    qp = range(10, 20)
    qc = range(20, 30)

    xlabel = "time [h]"
    ylabel = "drug mass [ng]"

    fig = plot_data(t, qp, qc)
    
    #extract axis object
    ax = fig.gca()

    #assert the labels are correct
    assert ax.get_xlabel() == xlabel
    assert ax.get_ylabel() == ylabel


