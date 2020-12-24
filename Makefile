all: prettier

prettier:
	@prettier --write "**/*.{sh,md,py}"