require 'MetaData2'
require 'Upload2'
require 'Shortcuts'
require 'LaTeX2'
require 'Image2'
require 'Contracts'


meta_object do
  extend MetaData2
  extend LaTeX2::Actions
  extend Upload2::Actions
  extend Shortcuts::Actions

  inherit_remote_directory

  def render_pngs
  end
  
  bind( { :png => make_action(description: 'Generate pngs') do
            `python generate-graphs.py`
          end } )

  quick_all_tex
  quick_all(:png, :pdf)
end
