from openerp.osv import osv,fields
import openerp

class model_astrazenica(osv.osv):
    _name="twitter.astrazenica"
    _columns={
        'tweet':fields.char("Tweet",required=True),
        'polarite':fields.float("Polarite",required=True)
    }
    def create(self, cr, uid, values, context=None):
        self.pool.get("twitter.astrastatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.neutrestatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.positifstatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.negatifstatistic").create(cr, uid, {}, context=context)
        return super(model_astrazenica, self).create(cr, uid, values, context=context)
    def write(self, cr, uid,ids, values, context=None):
        out=super(model_astrazenica, self).write(cr, uid,ids, values, context=context)
        self.pool.get("twitter.neutrestatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.positifstatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.negatifstatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.astrastatistic").create(cr, uid, {}, context=context)
        return out
    def unlink(self, cr, uid, values, context=None):
        out=super(model_astrazenica, self).unlink(cr, uid, values, context=context)
        self.pool.get("twitter.neutrestatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.positifstatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.negatifstatistic").create(cr, uid, {}, context=context)
        self.pool.get("twitter.astrastatistic").create(cr, uid, {}, context=context)
        return out
model_astrazenica()