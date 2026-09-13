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

# Dependências vindas dos próprios documentos: um PDF precisa ser refeito quando
# muda qualquer arquivo que ele inclua com \input, direta ou indiretamente
# (o ofício inclui base_empresa.tex, que inclui contatos_brasil.tex, e assim por
# diante). Listar isso à mão deixa o build servindo PDF desatualizado em silêncio.
entradas = $(shell sed -n 's/%.*//; s/.*\\input{\([^}]*\)}.*/\1/p' $(1) 2>/dev/null)
nivel2   = $(foreach f,$(call entradas,$(1)),$(f) $(call entradas,$(f)))
deps     = $(sort $(foreach f,$(call nivel2,$(1)),$(f) $(call entradas,$(f))))

# Duas passagens: sumário, longtable e \pageref{LastPage} só fecham na segunda.
define regra
$(BUILD)/$(notdir $(1:.tex=.pdf)): $(1) $(call deps,$(1))
	@mkdir -p $$(BUILD)
	@$$(LATEX) $$(LATEXFLAGS) -output-directory=$$(BUILD) $$< > /dev/null
	@$$(LATEX) $$(LATEXFLAGS) -output-directory=$$(BUILD) $$< > /dev/null
	@echo "  PDF  $$@"
endef

$(foreach s,$(SOURCES),$(eval $(call regra,$(s))))

clean:
	rm -rf $(BUILD)
