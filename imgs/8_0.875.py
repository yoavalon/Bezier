d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.long)

d.end()
