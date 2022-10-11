d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.low)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.S, Length.medium)

d.end()
