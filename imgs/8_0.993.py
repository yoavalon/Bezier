d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.medium)

d.end()
