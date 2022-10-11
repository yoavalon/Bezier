d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
