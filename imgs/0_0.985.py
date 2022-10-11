d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.position_pen(2,3)
d.curve(Direction.NW, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(0,2)

d.end()
