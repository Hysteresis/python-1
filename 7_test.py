# %% [markdown]
# # Variable

# %% [markdown]
# Create a variable named day, which contained the numeric value 1.

# %%


# %%
day = 1

# %% [markdown]
# Create a variable named month, which contained the string value January.

# %%
month = "January"

# %% [markdown]
# Create a variable named year, which contained the numeric value 2000.

# %%
year = 2000

# %% [markdown]
# Create a variable named elapsed_day, which contained the numeric value 1/365.

# %%
elapsed_day = 1 / 365

# %% [markdown]
# Print out the type of the created variables

# %%
print(type(day), type(month), type(year), type(elapsed_day))

# %% [markdown]
# Concatenate the created variable and print out a sentence like : "1 January 2000. Elapsed days : 0.003 percent"

# %%
print(f"{day} {month} {year}. Elapsed_days : {elapsed_day:.3f} percent")




