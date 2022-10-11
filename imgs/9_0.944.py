d = DslBezier()

d.position_pen(1,0)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)

d.end()
