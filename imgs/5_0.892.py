d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.position_pen(1,3)
d.position_pen(1,0)

d.end()
