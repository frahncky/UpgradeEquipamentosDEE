# Compilação dos documentos do repositório.
#
# Todos os documentos usam caminhos relativos à raiz (\input{modelos/preambulo.tex}),
# portanto o make precisa ser executado a partir desta pasta.
#
#   make            compila todos os PDFs em build/
#   make oficios    somente os 60 ofícios por empresa
#   make dossie     somente o dossiê institucional
#   make modelos    somente os documentos institucionais de modelos/
#   make diretorio  somente o diretório interno de contatos
#   make clean      remove build/

LATEX      := pdflatex
LATEXFLAGS := -interaction=nonstopmode -halt-on-error -file-line-error
BUILD      := build

MODELOS   := $(wildcard modelos/0*.tex)
OFICIOS   := $(wildcard empresas/[0-9]*.tex)
DOSSIE    := dossie/01_dossie_institucional.tex
DIRETORIO := empresas/diretorio_contatos.tex

SOURCES := $(MODELOS) $(OFICIOS) $(DOSSIE) $(DIRETORIO)
PDFS    := $(patsubst %.tex,$(BUILD)/%.pdf,$(notdir $(SOURCES)))

.PHONY: all oficios dossie modelos diretorio clean
all: $(PDFS)

oficios:   $(patsubst %.tex,$(BUILD)/%.pdf,$(notdir $(OFICIOS)))
dossie:    $(patsubst %.tex,$(BUILD)/%.pdf,$(notdir $(DOSSIE)))
modelos:   $(patsubst %.tex,$(BUILD)/%.pdf,$(notdir $(MODELOS)))
diretorio: $(patsubst %.tex,$(BUILD)/%.pdf,$(notdir $(DIRETORIO)))

# Duas passagens: sumário, longtable e \pageref{LastPage} só fecham na segunda.
define compilar
	@mkdir -p $(BUILD)
	@$(LATEX) $(LATEXFLAGS) -output-directory=$(BUILD) $< > /dev/null
	@$(LATEX) $(LATEXFLAGS) -output-directory=$(BUILD) $< > /dev/null
	@echo "  PDF  $@"
endef

COMUNS := modelos/preambulo.tex

$(BUILD)/%.pdf: modelos/%.tex $(COMUNS)
	$(compilar)

$(BUILD)/%.pdf: empresas/%.tex empresas/base_empresa.tex empresas/contatos_brasil.tex $(COMUNS)
	$(compilar)

$(BUILD)/%.pdf: dossie/%.tex dossie/corpo_docente.tex dossie/cenario_maranhao.tex dossie/fluxo_laboratorios.tex $(COMUNS)
	$(compilar)

clean:
	rm -rf $(BUILD)
