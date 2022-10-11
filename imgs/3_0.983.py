d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.NE, Length.long)

d.end()
