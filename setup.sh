#!/usr/bin/env bash

# Setup postgres database
createuser -d anthill_promo -U postgres
createdb -U anthill_promo anthill_promo