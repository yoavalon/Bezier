d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NW, Length.short)
d.position_pen(2,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)

d.end()
